##################################################
## Project: Working with NWM/NWIS NetCDF files
## Script purpose: Extraction from every site
## Date: 2020-02-22
##################################################
library(RNetCDF)
library(dplyr)
library(xlsx)


dir = '/Users/nodarsotkilava/Developer/water_ml/'
mapping    = readRDS( paste(dir,"mapping.rds", sep="") )
## establish netCDF connections
nwis       = open.nc( paste(dir,"nwis_v20_daily.nc", sep="") )
nwm        = open.nc( paste(dir,"nwm_v20_hourly.nc", sep="") )
site_cor = data.frame(Site_Number = integer(), Correlation = double())

for(i in 1:nrow(mapping)){
  test.site = mapping[i,]
  nwm_flow <- data.frame(
    #pull time from the nwm netcdf, these are hourly
    time = as.POSIXct(var.get.nc(nwm, "time"), origin = "1970-01-01", tz = 'UTC'),
    #pull streamflow data for one ID'd feature (nwm_retro_id), make sure to unpack!!!
    Q    = var.get.nc(nwm, "streamflow",
                      start = c(1, test.site$nwm_retro_id), count = c(NA, 1),
                      unpack = TRUE)) %>%
    # to align to daily NWIS, group by and summarize daily mean
    group_by(date   = as.Date(time)) %>%
    summarise(nwm_cms = mean(Q), comid = test.site$feature_id)
  
  usgs_flow = data.frame( # (actual stream/river measurements)
    #pull time from the nwis netcdf, these are daily
    date = as.Date(var.get.nc(nwis, "time"), origin = "1970-01-01", tz = 'UTC'),
    #pull streamflow data for one ID'd feature (nwis_retro_id), make sure to unpack!!!
    nwis_cms    = var.get.nc(nwis, "streamflow",
                             start = c(1, test.site$nwis_retro_id), count = c(NA, 1),
                             unpack = TRUE),
    site_id = test.site$site_no)
  
  # merge computer model and stream/river measurements by date and location
  final = merge(nwm_flow, usgs_flow, by = "date") %>% 
    select(comid, date, nwm_cms, nwis_cms) %>% 
    na.omit()
  
  #cor(final$nwm_cms, final$nwis_cms)
  
  #plot(final$date, final$nwm_cms, type = "l", ylim =c(0,300))
  #lines(final$date, final$nwis_cms, col  = "red")
  
  c <- tryCatch(
    expr = {
      cor(final$nwm_cms, final$nwis_cms)
    }, 
    warning = function(w){
      "Warning: SD is zero"
    }
  )
  site_cor[nrow(site_cor) + 1, ] = c(test.site$site_no, c)
}
write.xlsx(site_cor, "/Users/nodarsotkilava/Developer/water_ml/site_cor.xlsx")