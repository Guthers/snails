import React, { useEffect, useState } from 'react';
import QRCode from 'qrcode';
import { fetchEntries } from './Api';
import { EntryModel } from './models';

type Props = {
  entry: EntryModel
};

//TODO: Add api call

const generateQR = async (text: string) => {
  return await QRCode.toDataURL(text, { margin: 1, errorCorrectionLevel: 'L', width: 100 })
}

const Entry = (props: Props) => {
  const [qr, setQR] = useState("");

  useEffect(() => {
    generateQR("reddit.com").then(qr => setQR(qr))
  })

  return (
    <div className="m-2 p-5 text-2xl font-medium bg-teal-700 flex">
      <p className="font-bold max-w-xs mr-3">{props.entry.author.name} says {props.entry.content}</p>
      <div className="flex bg-gray-600 mx-2 self-end">
        <img src={qr} className="self-end max-w-xs" alt="qr code" />
      </div>
    </div>
  );
}

const Entries = () => {
  const [items, setItems] = useState<EntryModel[]>([]);

  useEffect(() => {
    const timer1 = setInterval(() => refresh(), 1000)

    return () => {
      clearInterval(timer1)
    }
  })

  const refresh = () => {
    fetchEntries().then(setItems)
  }


  return (
    <div className="flex-grow flex items-start flex-wrap overflow-hidden justify-center">
      {items.map(item => <Entry entry={item} />)}
    </div>
  )
}

export default Entries;
