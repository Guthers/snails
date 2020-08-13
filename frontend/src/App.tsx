import React from 'react';
import Bar from './Bar';
import Message from './Message';
import News from './News';
import Timetable from './Timetable';


function App() {
  return (
    <div className="h-screen bg-black grid grid-cols-2 lg:grid-cols-4 grid-rows-3 lg:grid-rows-2 text-white gap-5 p-5">
      <div className="relative flex col-span-2 lg:col-span-3">
        <div className="absolute inset-x-0">
          <Bar time="13:06" date="5/12/2020" temperature="31°C" weather="Cloudy"/>
        </div>
          <News image="https://images.unsplash.com/photo-1511447333015-45b65e60f6d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2623&q=80" title="Into the Unknown"/>
      </div>

      <div className="row-span-1 lg:row-span-2 bg-green-900">
            <Timetable/>
      </div>

      <div className="bg-snail-gray-800 overflow-hidden">
      </div>

      <div className="bg-snail-gray-800 overflow-hidden">
      </div>

      <div className="bg-snail-gray-800 overflow-hidden">
        <div className="m-5">
          <div className="my-3">
            <Message message="What is the most disorganised course and why is it DECO3801?"/>
          </div>
          <div className="my-3">
            <Message message="Best coffee on campus?"/>
          </div>
        </div>
      
      </div>
    </div>
  );
}

export default App;
