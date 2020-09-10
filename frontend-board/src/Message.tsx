import React, { useEffect, useState } from 'react';
import QRCode from 'qrcode';

type Props = {
  message: string
};

const generateQR = async (text: string) => {
    return await QRCode.toDataURL(text, {margin: 1, errorCorrectionLevel: 'L', width: 100})
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
      <img src={qr} className="self-end max-w-xs" alt="qr code"/>
    </div>
  </div>
  );
}

const Messages: React.FC = (props) => {
  return (
  <div className="flex-grow flex items-start flex-wrap overflow-hidden justify-center">
    <Message message="What is the most unorganized course and why is it DECO3801?"/>
    <Message message="Why did that teacher get fired from your school?"/>
    <Message message="What has no right to be as difficult as it is?"/>
    <Message message="How do you stop the 'Most humans suck' mentality?"/>
    <Message message="What’s the most overpriced thing you’ve seen?"/>
    <Message message="What are you happy about right now?"/>
    <Message message="Why is ITEE trash?"/>
  </div>
  )
}

export default Messages;