export type EntryId = string
export type UserId = string

export interface EntryModel {
  content: string
  created_at: Date
  entry_id: EntryId
  liked_by: UserModel[]
  replies: EntryId[]
  reply_to?: EntryId
  author: UserModel
}

export interface NewsModel {
  content: string
  created_at: Date
  image_url: string | null
  news_id: string
  title: string
  url: string
}

export interface WeatherModel {
  conditions: string | null
  created_at: string
  current_temperature: number | null
  humidity: number | null
  max_temperature: number | null
  min_temperature: number | null
  precipitation: number | null
  prob_precipitation: number | null
  uv_index: number | null
}

export interface UserModel {
  created_at: Date
  name: string
  username: string
  user_id: UserId
}