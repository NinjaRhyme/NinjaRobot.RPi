var path = require('path');
var webpack = require('webpack');

module.exports = {
  resolveLoader: {
    root: path.join(__dirname, 'node_modules')
  },
  entry: {
    bundle: [path.join(__dirname, '/Static/js/index.js')],
  },
  output: {
    path: __dirname,
    filename: '/Static/build/[name].js',
    publicPath: '/build'
  },
  module: {
    loaders: [{
      test: /\.js$/,
      loader: "babel?presets[]=react,presets[]=es2015",
      exclude: /node_modules/,
      include: path.join(__dirname, '/Static')
    }, {
      test: /\.css$/,
      loader: "css-loader",
      exclude: /node_modules/,
      include: path.join(__dirname, '/Static')
    }]
  }
};
