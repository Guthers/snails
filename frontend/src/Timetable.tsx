import React from 'react';

function Timetable() {
  const LAKES = [
    ["66", "ARR"],
    ["28", "ARR"],
    ["169", "2 min"],
    ["169", "3 min"],
    ["29", "10 min"],
  ];
  const CHANCELLORS = [
    ["412", "1 min"],
    ["402", "5 min"],
    ["411", "6 min"],
    ["432", "10 min"],
    ["427", "15 min"],
  ];
  return (
  <div className="flex flex-col text-center">
    <h1 className="text-5xl font-bold text-center tracking-tight">Timetable</h1>
    <div className ="flex-grow grid grid-rows-2">

      <div>
      <h2 className="text-3xl font-bold">UQ Lakes</h2>
      {
        LAKES.map(([x, y], i) => {
          return <TimetableEntry routeCode={x} eta={y}/>
        })
      }
      </div>
      <div>
      <h2 className="text-3xl font-bold">Chancellor's Place</h2>
      {
        CHANCELLORS.map(([x, y], i) => {
          return <TimetableEntry routeCode={x} eta={y}/>
        })
      }
      </div>
      </div>
  </div>
  );
}

type TimetableEntryProps = {
  routeCode: string,
  eta: string,
}

function TimetableEntry(props: TimetableEntryProps) {
  return <div className="flex justify-between text-3xl">
    <span className="font-black">{props.routeCode}</span>
    <span className="font-black">{props.eta}</span>
  </div>
}

export default Timetable;
