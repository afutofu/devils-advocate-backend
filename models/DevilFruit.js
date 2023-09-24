const mongoose = require("mongoose");

const DevilFruitSchema = mongoose.Schema({
  fruit_type: {
    type: String,
  },
  name: {
    type: String,
  },
  price: {
    type: Number,
  },
  imagelink: {
    type: String,
  },
  english_name: {
    type: String,
  },
  meaning: {
    type: String,
  },
  info: {
    type: String,
  },
});

module.exports = mongoose.model("devilfruit", DevilFruitSchema);
