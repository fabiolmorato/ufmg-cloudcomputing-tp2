import api from "./api";

export async function isAmericanTweet(tweet) {
  const response = await api.post("/api/american", {
    text: tweet
  });

  const { data } = response;

  return {
    isAmerican: data.is_american,
    version: data.version,
    modelDate: data.model_date
  };
}
