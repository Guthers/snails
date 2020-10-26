import React, { useEffect, useState } from 'react';
import QRCode from 'qrcode';
import { fetchEntries } from './Api';

type Props = {
  message: string
};

//TODO: Add api call

const generateQR = async (text: string) => {
  return await QRCode.toDataURL(text, { margin: 1, errorCorrectionLevel: 'L', width: 100 })
}

function Message(props: Props) {
  const [qr, setQR] = useState("");

  useEffect(() => {
    generateQR("reddit.com").then(qr => setQR(qr))
  })

  return (
    <div className="m-2 p-5 text-2xl font-medium bg-teal-700 flex">
      <p className="font-bold max-w-xs mr-3">{props.message}</p>
      <div className="flex bg-gray-600 mx-2 self-end">
        <img src={qr} className="self-end max-w-xs" alt="qr code" />
      </div>
    </div>
  );
}

const Messages: React.FC = () => {
  const defaultItems: string[] = [];
  const [items, setItems] = useState(defaultItems);

  useEffect(() => {
    fetchEntries().then(response => {
      response.json().then(data => {
        var newItems: string[] = [];
        data.forEach((entry: { [x: string]: any }) => {
          newItems.push(`${entry["author"]["name"]} says '${entry["content"]}'`)
        });
        setItems(newItems);
      })
    })
  })

  return (
    <div className="flex-grow flex items-start flex-wrap overflow-hidden justify-center">
      {items.map(item => <Message message={item} />)}
    </div>
  )
}

export default Messages;
