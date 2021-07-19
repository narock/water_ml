library(dplyr)

dir1 = "D:\\Developer\\water_ml\\Data\\Bias_By_Year\\Fall\\"
dir2 = "D:\\Developer\\water_ml\\Data\\Bias_By_Year\\Winter\\"
dir3 = "D:\\Developer\\water_ml\\Data\\Bias_By_Year\\Spring\\"
dir4 = "D:\\Developer\\water_ml\\Data\\Bias_By_Year\\Summer\\"

out1 = "D:\\Developer\\water_ml\\Data\\Bias_plots\\Fall\\"
out2 = "D:\\Developer\\water_ml\\Data\\Bias_plots\\Winter\\"
out3 = "D:\\Developer\\water_ml\\Data\\Bias_plots\\Spring\\"
out4 = "D:\\Developer\\water_ml\\Data\\Bias_plots\\Summer\\"

starting_year = 1995

for(i in 0:22){
  
  data1 = read.csv( paste(dir1, "fall_", (i + starting_year), ".csv",sep=""), na = "NA" )
  data2 = read.csv( paste(dir2, "winter_", (i + starting_year), ".csv",sep=""), na = "NA" )
  data3 = read.csv( paste(dir3, "spring_", (i + starting_year), ".csv",sep=""), na = "NA" )
  data4 = read.csv( paste(dir4, "summer_", (i + starting_year), ".csv",sep=""), na = "NA" )
  
  data1 = data1 %>% pull(bias)
  data2 = data2 %>% pull(bias)
  data3 = data3 %>% pull(bias)
  data4 = data4 %>% pull(bias)
  
  png(file = paste(out1, "fall_", (i + starting_year), ".png"))
  boxplot(data1, main = paste("fall_",(i + starting_year)))
  dev.off()
  
  png(file = paste(out2, "winter_", (i + starting_year), ".png"))
  boxplot(data2, main = paste("winter_",(i + starting_year)))
  dev.off()
  
  png(file = paste(out3, "spring_", (i + starting_year), ".png"))
  boxplot(data3, main = paste("spring_",(i + starting_year)))
  dev.off()
  
  png(file = paste(out4, "summer_", (i + starting_year), ".png"))
  boxplot(data4, main = paste("summer_",(i + starting_year)))
  dev.off()
}

