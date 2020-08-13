import React from 'react';

type Props = {
  time: string,
  date: string,
  temperature: string,
  weather: string,
}

function Bar(props: Props) {
  return (
  <div>
    <div className="font-black text-3xl font-mono text-center lg:text-left bg-black bg-opacity-50 p-3 px-5 tracking-tight">
      <span className="mr-6">{props.time}</span>
      <span className="mr-6">{props.date}</span>
      <span className="mr-6">{props.temperature}</span>
      <span className="mr-6">{props.weather}</span>
    </div>
  </div>
  );
}

export default Bar;

