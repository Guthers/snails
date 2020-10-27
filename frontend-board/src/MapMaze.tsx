import React, { useRef, useState, useLayoutEffect } from 'react';

//TODO: Add api call

const MapMaze: React.FC = () => {
  const ref = useRef<HTMLDivElement>(null);
  const [width, setWidth] = useState(0);
  const [height, setHeight] = useState(0);

  useLayoutEffect(() => {
    if(ref.current) {
      setHeight(ref.current.clientHeight);
      setWidth(ref.current.clientWidth);
      console.log(width + " " + height)
    }

    const handleWindowResize = () => {
      if(ref.current) {
        setHeight(ref.current.clientHeight);
        setWidth(ref.current.clientWidth);
      }
    };

    window.addEventListener("resize", handleWindowResize);

    return () => window.removeEventListener("resize", handleWindowResize);
  }, [height, width]);

  return (
  <div ref={ref} className="flex-grow">
    <iframe 
      title="map"
      width={width}
      height={height+30}
      frameBorder={0}
      scrolling="no" 
      marginHeight={0}
      marginWidth={0}
      src="https://use.mazemap.com/embed.html#config=uq&v=1&zlevel=1&campuses=uq&campusid=406&center=153.013785,-27.500020&zoom=18&utm_medium=iframe" 
      allow="geolocation"></iframe>
  </div>
  );
}

export const Discord: React.FC = () => {
  const ref = useRef<HTMLDivElement>(null);
  const [width, setWidth] = useState(0);
  const [height, setHeight] = useState(0);

  useLayoutEffect(() => {
    if(ref.current) {
      setHeight(ref.current.clientHeight);
      setWidth(ref.current.clientWidth);
      console.log(width + " " + height)
    }

    const handleWindowResize = () => {
      if(ref.current) {
        setHeight(ref.current.clientHeight);
        setWidth(ref.current.clientWidth);
      }
    };

    window.addEventListener("resize", handleWindowResize);

    return () => window.removeEventListener("resize", handleWindowResize);
  }, [height, width]);
  return (
    <div ref={ref} className="flex-grow">
      <iframe 
      title="discord"
      src="https://discordapp.com/widget?id=740729750775005245&theme=dark" 
      width={width}
      height={height}
      allowTransparency={true}
      frameBorder={0} 
      sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe>
      </div>
  );
}
export default MapMaze;
