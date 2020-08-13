import React from 'react';

type Props = {
  message: string
};

function Message(props: Props) {
  return (
  <div className="p-3 text-2xl font-medium bg-blue-800 grid grid-cols-3-1">
    <p>{props.message}</p>
    <div className="flex bg-gray-600 mx-2">
      <img src="https://via.placeholder.com/100" className="self-end"/>
    </div>
  </div>
  );
}

export default Message;