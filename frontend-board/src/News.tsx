import React, { useState, useEffect } from 'react';
import { fetchNews } from './Api';

const default_img = "https://images.unsplash.com/photo-1511447333015-45b65e60f6d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2623&q=80";

const News: React.FC = () => {
  const defaultItems: { [x: string]: string }[] = [{ "image": default_img, "title": "Into the unknown!" }];
  const [items, setItems] = useState(defaultItems);

  useEffect(() => {
    fetchNews().then(response => {
      response.json().then(data => {
        var newItems: { [x: string]: string }[] = [];
        data.forEach((article: { [x: string]: string }) => {
          var newItem: { [x: string]: string } = {};
          newItem["image"] = article["image_url"] ? article["image_url"] : default_img;
          newItem["title"] = article["title"];
          newItems.push(newItem);
        });
        console.log("Updated to " + newItems.length + " items")
        setItems(newItems);
      })
    })
  })

  console.log(items)
  return (
    <div className="flex flex-grow overflow-hidden bg-cover bg-center p-5 items-end"
      style={{ backgroundImage: `url(${items[0]["image"]})`, backgroundColor: '#ddd', backgroundBlendMode: 'multiply' }}
    >
      <h1 className="font-black text-6xl tracking-tight text-shadow-md">{items[0]["title"]}</h1>
    </div>
  )
}

export default News;