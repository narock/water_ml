#NOTE: This does not produce excel of the summary statistic

dir1 = "D:\\Developer\\water_ml\\Data\\Bias_By_Year\\Fall\\"
dir2 = "D:\\Developer\\water_ml\\Data\\Bias_By_Year\\Winter\\"
dir3 = "D:\\Developer\\water_ml\\Data\\Bias_By_Year\\Spring\\"
dir4 = "D:\\Developer\\water_ml\\Data\\Bias_By_Year\\Summer\\"

starting_year = 1995

for(i in 0:22){
  
  data1 = read.csv( paste(dir1, "fall_", (i + starting_year), ".csv",sep=""), na = "NA" )
  data2 = read.csv( paste(dir2, "winter_", (i + starting_year), ".csv",sep=""), na = "NA" )
  data3 = read.csv( paste(dir3, "spring_", (i + starting_year), ".csv",sep=""), na = "NA" )
  data4 = read.csv( paste(dir4, "summer_", (i + starting_year), ".csv",sep=""), na = "NA" )
  
  data1 = data1[complete.cases(data1), ]
  data2 = data2[complete.cases(data2), ]
  data3 = data3[complete.cases(data3), ]
  data4 = data4[complete.cases(data4), ]
  
  print(paste("fall ", (i + starting_year)))
  print(summary(data1$bias))
  print(paste("winter " , (i + starting_year)))
  print(summary(data2$bias))
  print(paste("spring " ,(i + starting_year)))
  print(summary(data3$bias))
  print(paste("summer ", (i + starting_year)))
  print(summary(data4$bias))
  
}
