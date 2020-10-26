import React, { useState, useEffect } from 'react';

const PanelPadding = [ 'p-0', 'p-1', 'p-2', 'p-3', 'p-4', 'p-5', 'p-6' ] as const; 
const PanelMargin = [ 'm-0', 'm-1', 'm-2', 'm-3', 'm-4', 'm-5', 'm-6' ] as const; 
const PanelBorderRadius = [ 'rounded-none', 'rounded-sm', 'rounded', 'rounded-md', 'rounded-lg' ] as const;

type Props = {
  padding?: typeof PanelPadding[number],
  margin?: typeof PanelMargin[number],
  borderRadius?: typeof PanelBorderRadius[number],
  isEdit?: boolean,
  background?: boolean,
};

/**
 * An unpadded wrapper for dashboard items
 */
export const Panel: React.FC<Props> = (props) => {
  const padding = props.padding ?? '';
  const margin = props.margin ?? '';
  const borderRadius = props.borderRadius ?? '';
  const background = props.background ? '':  'bg-gray-800'

  return (
      <div className={`h-full relative flex overflow-hidden 
                            ${padding} ${margin} ${background} ${borderRadius}`
                          }>
        {props?.isEdit?<div className="absolute top-0 right-0 mt-4 mr-4">Editing</div>:null}
        {props.children}
      </div>
  )
}