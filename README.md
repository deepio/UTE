# UTE
**U**nittest **T**raining **E**xamples

There are commonly 3 types of unit tests, and they each seek to answer different questions.

#### Regression testing
  - If I update my dependencies, does my application still work?
  - If I update my OS, does my application still work?

#### Integration testing
  - If I change this base class, will it break all the classes that inherit from it?
  - Does this code still work? Do all functions still have the ability to communicate with each other? 
Integration testing makes it difficult for codebreaking faults to get pushed to a version control system, but only if you write a test for each. You can automatically test on every commit, prior to accepting a branch merge, only on pull requests, or any combination of these by using a service like `travis`, `appveyor` or `circleci`.

#### Acceptance testing
  - Do these features follow the vision of the project?
  - Are these features worth the time required to implement in this project?
