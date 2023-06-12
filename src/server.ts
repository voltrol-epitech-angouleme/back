// import express from 'express';

// const app = express();
// const port = process.env.PORT || 3000;

// app.get('/api', (req, res) => {
//   res.json({ message: 'Hello, world!' });
// });

// app.listen(port, () => {
//   console.log(`Server is running on port ${port}`);
// });

import http from 'http';

const server: any = http.createServer((req, res) => {
  res.end('Hello, world!');
});

server.listen(3000, () => {
  console.log('Server is running on port 3000');
});
