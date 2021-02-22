##################################################
## Project: Working with NWM/NWIS NetCDF files
## Script purpose: Sample extraction
## Date: 2020-01-11
##################################################
library(RNetCDF)
library(dplyr)

# You will need the files I shared with you and to update these paths
## load data
dir = '/Users/nodarsotkilava/Developer/water_ml/'
mapping    = readRDS( paste(dir,"mapping.rds", sep="") )
## establish netCDF connections
nwis       = open.nc( paste(dir,"nwis_v20_daily.nc", sep="") )
nwm        = open.nc( paste(dir,"nwm_v20_hourly.nc", sep="") )

# Starting with a random site, this is just for example
(test.site = mapping[1000,])

# get nwm v2.0 flows (computer simulation)
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

cor(final$nwm_cms, final$nwis_cms)

plot(final$date, final$nwm_cms, type = "l", ylim =c(0,300))
lines(final$date, final$nwis_cms, col  = "red")

c = cor(final$nwm_cms, final$nwis_cms)
cat("Correlation between model and stream measurements:", c)
print(" ")
cat("Correlation computed at site:", test.site$site_no)
