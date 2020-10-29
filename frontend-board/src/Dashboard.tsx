/**
 * TODO:
 * Fix wrappers
 * Set up sensible default layouts
 * Crete HOCs for GridItem
 * Look into using a different grid library. RGL is slow :(
 * Bounded height
 * Force redraw children on resize
 */
import React, { useState, useEffect } from 'react';
import { WidthProvider, Responsive, Layouts, Layout } from 'react-grid-layout';

const ResponsiveReactGridLayout = WidthProvider(Responsive);

type Props = {
  panels: Map<string, JSX.Element>,
  isEdit: boolean,
};

/**
 * A drag-and-drop enabled 2-dimensional grid.
 * Changes to the layout are saved in local storage.
 * 
 * Type `localstorage.clear()` in the Developer Console to reset the layout to default
 */
const Dashboard: React.FC<Props> = (props) => {
    const [height, setHeight] = useState(window.innerHeight);

    const defaultLayout = {
      lg:[
        {i: "a", x:6, y:0, w:2, h:10},
        {i: 'b', x:0, y:0, w:6, h:6},
        {i: 'c', x:0, y:6, w:4, h:4},
        {i: 'd', x:4, y:4, w:2, h:4},
        {i: 'e', x:4, y:6, w:2, h:4},
        {i: 'f', x:0, y:0, w:4, h:6},
      ],
      sm:[
        {i: "a", x:0, y:4, w:1, h:6},
        {i: 'b', x:0, y:0, w:2, h:4},
        {i: 'c', x:1, y:4, w:1, h:4},
        {i: 'd', x:1, y:8, w:1, h:2},
        {i: 'e', x:2, y:8, w:1, h:2},
        {i: 'f', x:0, y:0, w:2, h:4},
      ],
    }

    const layout = localStorage.getItem("layout") ? JSON.parse(localStorage.getItem("layout")!) : defaultLayout;
    const onLayoutChange = (_currentLayout: Layout[], allLayouts: Layouts) => localStorage.setItem("layout", JSON.stringify(allLayouts))

    useEffect(() => {
      const handleWindowResize = () => {
        setHeight(window.innerHeight);
      };

      window.addEventListener("resize", handleWindowResize);

      return () => window.removeEventListener("resize", handleWindowResize);
    }, []);

    // RGL does not have support for bounded height grid.
    // Do some calculation to force (this div's) height to the parent height
    const rows = 10;
    const [marginX, marginY] = [15, 15];
    const [paddingX, paddingY] = [30, 30]
    const rowHeight = (height / rows) - (marginY * (rows - 1) / rows) - (paddingY * 2 / rows)

    return (
      <ResponsiveReactGridLayout 
        cols={{lg: 8, md:4, sm:2, xs:2, xxs:1}}
        rowHeight={rowHeight}
        layouts={layout}
        margin={[marginX,marginY]}
        containerPadding={[paddingX, paddingY]}
        onLayoutChange={onLayoutChange}
        isDraggable={props.isEdit}
        isResizable={props.isEdit}
        className="w-full bg-snail-gray text-white">
          {
          Array.from(props.panels, ([key, value]) => 
            <div key={key}>
              {React.cloneElement(value, {isEdit: props.isEdit})}
            </div>)
          }
      </ResponsiveReactGridLayout>
    );
}
export default Dashboard;
