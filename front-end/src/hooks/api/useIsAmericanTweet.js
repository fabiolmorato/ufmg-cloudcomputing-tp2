import useAsync from "../useAsync";

import * as api from "../../services/api/isAmerican";

export default function useIsAmericanTweet() {
  const {
    data: isAmerican,
    errorIsAmerican,
    loadingIsAmerican,
    act: checkIsAmerican
  } = useAsync(api.isAmericanTweet, false);

  return {
    isAmerican,
    errorIsAmerican,
    loadingIsAmerican,
    checkIsAmerican
  };
}
