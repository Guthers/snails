import { EntryModel, NewsModel, VehicleModel, WeatherModel } from "./models";

export const API_BASE = "https://deco3801-the-snails.uqcloud.net/api/";

export const getEndpoint = (end_point: string) : string =>
  API_BASE + end_point


export const fetchNews = () : Promise<NewsModel[]> => 
  fetch(getEndpoint("news"))
    .then(response => response.json())

export const fetchWeather = () : Promise<WeatherModel> => 
  fetch(getEndpoint("weather"))
    .then(response => response.json())

export const fetchEntries = () : Promise<EntryModel[]> => 
  fetch(getEndpoint("entries"))
    .then(response => response.json())

export const fetchLakes = () : Promise<VehicleModel[]> => 
  fetch(getEndpoint("transport/lakes"))
    .then(response => response.json())

export const fetchChancellors = () : Promise<VehicleModel[]> => 
  fetch(getEndpoint("transport/chancellors"))
    .then(response => response.json())