import postsModel, { PostsModel } from "./post"

export interface StoreModel {
  posts: PostsModel
}

const storeModel: StoreModel = {
  posts: postsModel
}

export default storeModel