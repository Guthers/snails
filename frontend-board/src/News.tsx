import React, { useState, useEffect } from 'react';
import { fetchNews } from './Api';
import { NewsModel } from './models';

const default_img = "https://images.unsplash.com/photo-1511447333015-45b65e60f6d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2623&q=80";

const News: React.FC = () => {
  const defaultItems: NewsModel[] = [{
    content: "Into the Unknown",
    created_at: new Date(),
    image_url: "",
    news_id: "foo",
    title: "Into the Unknown",
    url: "https://example.com"
  }]

  const [items, setItems] = useState<NewsModel[]>(defaultItems);
  const [activeItem, setActiveItem] = useState(0)

  useEffect(() => {
    refresh()
    const timer1 = setInterval(() => refresh(), 60000)
    const timer2 = setInterval(() => {
      setActiveItem(i => (i+1) % 5)
    }, 5000)

    return () => {
      clearInterval(timer1)
      clearInterval(timer2)
    }
  }, [])

  const refresh = () => {
    fetchNews().then(setItems)
  }

  return (
    <div className="flex flex-grow overflow-hidden bg-cover bg-center p-5 items-end"
      style={{ 
        backgroundImage: `url('${items && items[activeItem] && items[activeItem].image_url ? items[activeItem].image_url : default_img}')`, 
        backgroundColor: '#ddd', 
        backgroundBlendMode: 'multiply' }}
    >
      <h1 className="font-black text-6xl tracking-tight text-shadow-md">{items[activeItem] && items[activeItem].title ? items[activeItem].title : "Into The Unknown"}</h1>
    </div>
  )
}

export default News;
