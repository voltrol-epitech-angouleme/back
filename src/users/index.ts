import * as functions from "firebase-functions";

export const helloWorld = functions.https.onRequest((request, response) => {
  const userName = request.query.name;
  functions.logger.info(`Hello logs! ${userName}`, { structuredData: true });
  response.send(`Hello ${userName} from Firebase!`);
});
