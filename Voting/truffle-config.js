module.exports = {
    networks: {
        development: {
            host: "127.0.0.1",     // Localhost (default: none)
            port: 7545,            // Standard Ganache UI port
            network_id: "*",       // Any network (default: none)
        },
    },
    compilers: {
        solc: {
            version: "0.8.0", // Update this to match the version specified in your contract
            // More compiler settings...
        }
    }
};