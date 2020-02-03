const express = require('express');

const router = express.Router();

router.use(express.static('public'));
router.use(express.static('src/views'));

router.get('/', (req, res) => {
  res.send('It works!');
});

module.exports = router;