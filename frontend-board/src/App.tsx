import React, { useState, useEffect } from 'react';
import Dashboard from './Dashboard';
import Timetable from './Timetable';
import Bar from './Bar';
import Nav from './Nav';
import News from './News';
import MapMaze from './MapMaze';
import Messages from './Message';
import { Panel } from './Panel';

const App: React.FC = () => {
  const [edit, setEdit] = useState(false);
  const [view, setView] = useState(false);
  const [alert, setAlert] = useState(false);

  useEffect(() => {
    if (view) {
      setAlert(true);
    }
  }, [view])

  const panels: Map<string, JSX.Element> = new Map([
    ["a",
      <Panel padding={"p-5"} borderRadius="rounded">
        <Timetable />
      </Panel>],
    ["b",
      <Panel borderRadius="rounded">
        <div className="absolute inset-x-0">
          <Bar />
        </div>
        <News />
      </Panel>],
    ["c",
      <Panel borderRadius="rounded">
        <Messages />
      </Panel>],
    ["d",
      <Panel borderRadius="rounded">
        <MapMaze />
      </Panel>],
    ["e",
      <Panel borderRadius="rounded">
      </Panel>
    ]
  ]);

  return (
    <div>
      {
        view
          ? null
          : <Nav editFn={() => setEdit(!edit)} viewFn={() => setView(!view)} />
      }
      <Dashboard isEdit={edit} panels={panels} />

      {
        alert
          ?
          <div className="bg-teal-100 border-t-4 border-teal-500 mt-32 text-teal-900 px-4 py-3 shadow-md absolute top-0"
            onClick={() => setAlert(!alert)}
            role="alert">
            <div className="flex">
              <div className="py-1"><svg className="fill-current h-6 w-6 text-teal-500 mr-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 17.07zm12.73-1.41A8 8 0 1 0 4.34 4.34a8 8 0 0 0 11.32 11.32zM9 11V9h2v6H9v-4zm0-6h2v2H9V5z" /></svg></div>
              <div>
                <p className="">Press ESC to exit full screen view.</p>
              </div>
            </div>
          </div>
          : null
      }
    </div>
  );
}

export default App;