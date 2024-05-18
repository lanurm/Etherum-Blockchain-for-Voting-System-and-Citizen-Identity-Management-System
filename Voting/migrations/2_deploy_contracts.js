
const Voting = artifacts.require("Voting");

module.exports = function (deployer) {
    deployer.deploy(Voting, ["Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal"]);
};
