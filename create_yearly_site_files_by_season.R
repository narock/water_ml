dir = "C:\\Users\\thnar001\\Git\\water_ml\\Data\\Sites_By_Season_and_Year\\"
out1 = "C:\\Users\\thnar001\\Git\\water_ml\\Data\\Fall\\"
out2 = "C:\\Users\\thnar001\\Git\\water_ml\\Data\\Winter\\"
out3 = "C:\\Users\\thnar001\\Git\\water_ml\\Data\\Spring\\"
out4 = "C:\\Users\\thnar001\\Git\\water_ml\\Data\\Summer\\"

file_list <- list.files(path=dir)

for ( i in 1:length(file_list) ) {
  
  # read this site file
  data = read.csv( paste(dir, file_list[i], sep = "") )
  
  # get site number from file name
  parts = strsplit(file_list[i],"\\.") 
  x = unlist(parts)
  parts = strsplit(x[1], "_")
  x = unlist(parts)
  site_no = x[2]
  
  # loop over all the years in this file
  for ( j in 1:length(data$year) ) {
    
    # output to appropriate file 
    line1 = paste(site_no, ",", data$fall[j], sep="")
    line2 = paste(site_no, ",", data$winter[j], sep="")
    line3 = paste(site_no, ",", data$spring[j], sep="")
    line4 = paste(site_no, ",", data$summer[j], sep="")
  
    outFile1 = paste(out1, "fall_", data$year[j], ".csv", sep="")
    outFile2 = paste(out2, "winter_", data$year[j], ".csv", sep="")
    outFile3 = paste(out3, "spring_", data$year[j], ".csv", sep="")
    outFile4 = paste(out4, "summer_", data$year[j], ".csv", sep="")
    
    write(line1, file=outFile1, append=TRUE)
    write(line2, file=outFile2, append=TRUE)
    write(line3, file=outFile3, append=TRUE)
    write(line4, file=outFile4, append=TRUE)
    
  }
    
}
