import React from 'react';

type Props = {
  editFn: () => void,
  viewFn: () => void,

};

const Nav: React.FC<Props> = (props) => {
  return (
    <div className="bg-gray-700">
      <div className="flex justify-end py-2 px-2">
        <button className="mr-4 bg-gray-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                onClick={props.editFn}
        >
          Edit
        </button>
        <button className="bg-gray-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                onClick={props.viewFn}
        >
          View Mode
        </button>
      </div>
    </div>
  )
}

export default Nav;