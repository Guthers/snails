export const API_BASE = "https://deco3801-the-snails.uqcloud.net/api/";

export function getEndpoint(end_point: string) {
  return API_BASE + end_point;
}

export function fetchWeather() {
  return fetch(getEndpoint("weather"));
}

export function fetchNews() {
  return fetch(getEndpoint("news"));
}

export function fetchEntries() {
  return fetch(getEndpoint("entries"));
}