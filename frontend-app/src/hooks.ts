import { createTypedHooks } from "easy-peasy";
import { StoreModel } from "./model/index";

const typedHooks = createTypedHooks<StoreModel>();

export const useStoreState = typedHooks.useStoreState;
export const useStoreAction = typedHooks.useStoreActions;
export const useStateDispatch = typedHooks.useStoreDispatch;