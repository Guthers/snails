import React, { useState, useEffect } from 'react';
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
    fetchWeather().then(res => {
      setTime(res.created_at.substr(0, 10))
      setDate(res.created_at.substr(11))
      if (res.current_temperature)
        setTemperature(res.current_temperature.toString() ?? "25")
      if (res.conditions)
        setWeather(res.conditions)
    })
  })

  return (
    <div className="font-black text-3xl font-mono text-center lg:text-left bg-black bg-opacity-50 p-3 px-5 tracking-tight">
      <span className="mr-6">{time}</span>
      <span className="mr-6">{date}</span>
      <span className="mr-6">{temperature}</span>
      <span className="mr-6">{weather}</span>
    </div>
  );
}

export default Bar;

