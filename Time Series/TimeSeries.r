rm(list = ls())
library(timeSeries)
library(forecast)


a <- ts(1:30, frequency=12, start=c(2011,3))
print(a)
str(a)
attributes(a)

plot(AirPassengers)

# decompose time series 
apts <- ts(AirPassengers, frequency=12)
f <- decompose(apts)

# seasonal figures
f$figure
plot(f$figure, type="b", xaxt="n", xlab="")

# get names of 12 months in English words
monthNames <- months(ISOdate(2011,1:12,1))

# label x-axis with month names 
# las is set to 2 for vertical label orientation
axis(1, at=1:12, labels=monthNames, las=1) 

plot(f)


####### FITTING ARIMA TO DATA #################
######## Adjusted for Seasonality ############
apts_sdj <- seasadj(stl(AirPassengers), s.window="periodic")
plot(apts_sdj)
acf(apts_sdj)
pacf(apts_sdj)
fit <- arima(AirPassengers, order=c(2,0,0))
accuracy(fit)
fore <- predict(fit, n.ahead=24)
# error bounds at 95% confidence level
U <- fore$pred + 2*fore$se
L <- fore$pred - 2*fore$se
ts.plot(AirPassengers, fore$pred, U, L, col=c(1,2,4,4), lty = c(1,1,2,2))
legend("topleft", c("Actual", "Forecast", "Error Bounds (95% Confidence)"),
       col=c(1,2,4), lty=c(1,1,2))

############# With seasonality ###########################
acf(apts)
pacf(apts)
fit <- arima(AirPassengers, order=c(2,0,0), list(order=c(2,1,0), period=12))
accuracy(fit)
fore <- predict(fit, n.ahead=24)
# error bounds at 95% confidence level
U <- fore$pred + 2*fore$se
L <- fore$pred - 2*fore$se
ts.plot(AirPassengers, fore$pred, U, L, col=c(1,2,4,4), lty = c(1,1,2,2))
legend("topleft", c("Actual", "Forecast", "Error Bounds (95% Confidence)"),
       col=c(1,2,4), lty=c(1,1,2))



######## AUTO FIT ARIMA ##########################
library(forecast)
fit1 <- ts(AirPassengers)

# Automated forecasting using an ARIMA model
fit1 <- auto.arima(AirPassengers)
accuracy(fit1)
fore <- predict(fit1, n.ahead=24)
# error bounds at 95% confidence level
U <- fore$pred + 2*fore$se
L <- fore$pred - 2*fore$se
ts.plot(AirPassengers, fore$pred, U, L, col=c(1,2,4,4), lty = c(1,1,2,2))
legend("topleft", c("Actual", "Forecast", "Error Bounds (95% Confidence)"),
       col=c(1,2,4), lty=c(1,1,2))




# simple exponential - models level
fit <- HoltWinters(apts, beta=FALSE, gamma=FALSE)
# double exponential - models level and trend
fit <- HoltWinters(apts, gamma=FALSE)
# triple exponential - models level, trend, and seasonal components
fit <- HoltWinters(apts)

# predictive accuracy
# predict next three future values
library(forecast)
f=forecast(fit, 3)
accuracy(f)
plot(forecast(fit, 3))

