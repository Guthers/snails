import React from 'react';

type Props = {
  image: string,
  title: string,
};

function News(props: Props) {
  return (
    <div className="flex flex-grow overflow-hidden bg-cover bg-center p-5 items-end"
         style={{backgroundImage: `url(${props.image})`, backgroundColor: '#ddd', backgroundBlendMode: 'multiply'}}
    >
      <h1 className="font-black text-6xl tracking-tight text-shadow-md">{props.title}</h1>
    </div>
  )
}

export default News;

