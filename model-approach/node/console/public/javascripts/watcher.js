const fs = require('fs')
const child = require('child_process')

// watch the target file
const watcher = fs.watch('script.js')
// create a child process for the target application
let currentChild = child.fork('script.js')

watcher.on('change', () => {
  // we assure we have only one child process at time
  if (currentChild) {
    currentChild.kill()
  }
  // reset the child process
  currentChild = child.fork('script.js')
})