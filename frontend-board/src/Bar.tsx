import React, { useState, useEffect } from 'react';
import { isConditionalExpression } from 'typescript';
import { fetchWeather } from './Api';

/**
 * An information bar showing time, date, temperature and weather
 * @param props Props
 */
const Bar: React.FC = () => {
  const [time, setTime] = useState("")
  const [date, setDate] = useState("")
  const [temperature, setTemperature] = useState("")
  const [weather, setWeather] = useState("")

  useEffect(() => {
    refresh()
    poll()

    const timer1 = setInterval(() => refresh(), 1000)
    const timer2 = setInterval(() => poll(), 5000)

    return () => {
      clearInterval(timer1)
      clearInterval(timer2)
    }
  }, [])

  const refresh = () => {
    const date = new Date()
    setTime(date.toLocaleTimeString())
    setDate(date.toDateString())
  }

  const poll = () => {
    fetchWeather().then(res => {
      console.log(res)
      if (res.current_temperature)
        setTemperature(res.current_temperature.toString() ?? "25")
      if (res.conditions)
        setWeather(weatherToEmoji(res.conditions))
    }).catch(res => console.log(res))
  }

  const weatherToEmoji = (conditions: string) => {
    const contains = (x: string) => conditions.toLowerCase().includes(x)
    if (contains("clear") || contains("sunny")) {
      return "☀️"
    } else if (contains("rain") || contains("showers")) {
      return "🌧️"
    } else if (contains("cloudy")) {
      return "☁️"
    } else if (contains("fog") || contains("haze")) {
      return "🌫️"
    } else if (contains("frost") || contains("snow")) {
      return "🌨️"
    } else if (contains("cyclone") || contains("storm")) {
      return "🌩️"
    } else if (contains("wind")) {
      return "🌬️"
    } else {
      return "☀️"
    }
  }

  return (
    <div className="flex font-black text-3xl justify-center lg:justify-between font-mono bg-black bg-opacity-50 p-3 px-5 tracking-tight">
      <div>
        <span className="mr-6">{time}</span>
        <span className="mr-6">{date}</span>
      </div>
      <div>
        <span className="ml-6">{temperature}°C</span>
        <span className="ml-6">{weather}</span>
      </div>
    </div>
  );
}

export default Bar;

