// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    // Structure to represent a candidate
    struct Candidate {
        uint256 id;
        string name;
        uint256 voteCount;
    }

    // Array to store candidates
    Candidate[] public candidates;

    // Mapping to track whether an address has already voted
    mapping(address => bool) public hasVoted;

    // Event to emit when a vote is cast
    event Voted(uint256 candidateId, address voter);

    // Modifier to check if the sender hasn't voted already
    modifier hasNotVoted() {
        require(!hasVoted[msg.sender], "You have already voted.");
        _;
    }

    // Constructor to initialize candidates
    constructor(string[] memory _candidateNames) {
        for (uint256 i = 0; i < _candidateNames.length; i++) {
            candidates.push(Candidate(i, _candidateNames[i], 0));
        }
    }

    // Function to cast a vote
    function vote(uint256 _candidateId) public hasNotVoted {
        require(_candidateId < candidates.length, "Invalid candidate ID.");
        candidates[_candidateId].voteCount++;
        hasVoted[msg.sender] = true;
        emit Voted(_candidateId, msg.sender);
    }

    // Function to get the total votes for a candidate
    function getTotalVotes(uint256 _candidateId) public view returns (uint256) {
        require(_candidateId < candidates.length, "Invalid candidate ID.");
        return candidates[_candidateId].voteCount;
    }
}
