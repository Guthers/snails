import React, { useState, useEffect } from 'react';
import { fetchNews } from './Api';
import { NewsModel } from './models';

const default_img = "https://images.unsplash.com/photo-1511447333015-45b65e60f6d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2623&q=80";

const News: React.FC = () => {
  const defaultItems: NewsModel[] = [{
    content: "Into the Unknown",
    created_at: new Date(),
    image_url: default_img,
    news_id: "foo",
    title: "Into the Unknown",
    url: "https://example.com"
  }]

  const [items, setItems] = useState<NewsModel[]>(defaultItems);

  useEffect(() => {
    fetchNews().then(setItems)
  }, [])

  console.log(items)


  return (
    <div className="flex flex-grow overflow-hidden bg-cover bg-center p-5 items-end"
      style={{ 
        backgroundImage: `url(${items[0].image_url ?? default_img})`, 
        backgroundColor: '#ddd', 
        backgroundBlendMode: 'multiply' }}
    >
      <h1 className="font-black text-6xl tracking-tight text-shadow-md">{items[0].title}</h1>
    </div>
  )
}

export default News;