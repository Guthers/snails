import React, { useState, useRef, useLayoutEffect, cloneElement, Children, isValidElement } from 'react';
import {LAKES, CHANCELLORS} from './data';

//TODO: Add api call

const Timetable: React.FC = () => {
  return (
  <div className="flex flex-grow flex-col overflow-hidden">
    <h1 className="text-5xl font-bold text-center tracking-tight">Timetable</h1>
    <ListContext>
      <List 
        title="Lakes" 
        elements={LAKES} 
        titleClass="text-3xl text-center font-bold" 
        elementsClass="flex justify-between text-3xl"/>
      <List 
        title="Chancellors Place" 
        elements={CHANCELLORS} 
        titleClass="text-3xl text-center font-bold" 
        elementsClass="flex justify-between text-3xl"/>
    </ListContext>
  </div>
  );
}

type ListContextProps = {
  children: React.ReactElement<ListProps>[];
  className?: string;
}

const ListContext: React.FC<ListContextProps> = (props) => {
  const ref = useRef<HTMLDivElement>(null);
  const [height, setHeight] = useState(0);
  const [numChildren, setNumChildren] = useState(0);

  useLayoutEffect(() => {
    if(ref.current) {
      setHeight(ref.current.clientHeight);
      setNumChildren(ref.current!.childElementCount)
    }

    const handleWindowResize = () => {
      if(ref.current) {
        setHeight(ref.current.getBoundingClientRect().height);
      }
    };

    window.addEventListener("resize", handleWindowResize);

    return () => window.removeEventListener("resize", handleWindowResize);
  }, [height, numChildren]);

  return (
    <div ref={ref} className={"h-full " + props.className}>
      {
      Children.map(props.children, child =>
          isValidElement(child) ? cloneElement(child, {items: Math.floor(height/numChildren/39) - (child.props.title ? 1 : 0)}) : null
      )
      }
    </div>
  )
}

type ListProps = {
  className?: string,
  title?: string,
  titleClass?: string,
  elements:[string, string][],
  elementsClass?: string,
  items?: number,
}

const List: React.FC<ListProps> = (props) => {
  return <div className={props.className}>
    {
      props.title ? <h2 className={props.titleClass}>{props.title}</h2> : null
    }
    {
      props.elements.slice(0, props.items).map(([routeCode, eta], i) => {
          return <ListItem className={props.elementsClass} routeCode={routeCode} eta={eta} key={i}/>
      })
    }
  </div>
}

type ListItemProps = {
  routeCode: string,
  className?: string,
  eta: string,
}

const ListItem: React.FC<ListItemProps> = (props) => {
  return <div className={props.className}>
    <span className="font-black">{props.routeCode}</span>
    <span className="font-black">{props.eta}</span>
  </div>
}

export default Timetable;
