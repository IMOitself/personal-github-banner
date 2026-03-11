// ngl this was guided by gemini ai
// in fixing env file for 'GraphQL: Language Feature Support' extension.
const fs = require('fs');

if (fs.existsSync('.env')) {
  const envFile = fs.readFileSync('.env', 'utf8');

  envFile.split('\n').forEach(line => {
    const [key, ...value] = line.split('=');
    if (key && value.length > 0) 
      process.env[key.trim()] = value.join('=').trim();
  });
}

module.exports = {
  schema: [
    {
      "https://api.github.com/graphql": {
        headers: {
          Authorization: `Bearer ${process.env.ACCESS_TOKEN}`,
          "User-Agent": "VSCode-GraphQL-Extension"
        }
      }
    }
  ],
  documents: '**/*.graphql'
};