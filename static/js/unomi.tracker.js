var path = location.pathname + location.hash;
var keywords = ["Review", "Rating", "Machine learning"]
var unomiOption = {
  scope: "ryr",
  url: "http://localhost:8181", // we use an empty URL to make it relative to this page.
  initialPageProperties: {
    path: path,
    pageInfo: {
      pageId: path,
      pageName: document.title,
      destinationURL: location.href,
      referringURL: location.referrer,
      tags: keywords,
      categories: keywords,
    }
  },
};

window.unomiTracker || (window.unomiTracker = {});

(function () {
  var unomiTracker_queue = [];
  var methods = [
    "trackSubmit", "trackClick", "trackLink", "trackForm", "initialize", 
    "pageview", "identify", "reset", "group", "track", "ready", "alias", 
    "debug", "page", "once", "off", "on", "personalize"
  ];

  var factory = function (method) {
    return function () {
      var args = Array.prototype.slice.call(arguments);
      args.unshift(method);
      unomiTracker_queue.push(args);
      return window.unomiTracker;
    };
  };

  // For each of our methods, generate a queueing stub.
  for (var i = 0; i < methods.length; i++) {
    var method = methods[i];
    window.unomiTracker[method] = factory(method);
  }

  function callback(e) {
    unomiTracker.initialize({
      "Apache Unomi": unomiOption,
    });

    // Loop through the interim analytics queue and reapply the calls to their
    // proper analytics.js method.
    while (unomiTracker_queue.length > 0) {
      var item = unomiTracker_queue.shift();
      var method = item.shift();
      if (unomiTracker[method]) {
        unomiTracker[method].apply(unomiTracker, item);
      }
    }
  }

  // Define a method to load Analytics.js from our CDN,
  // and that will be sure to only ever load it once.
  unomiTracker.load = function () {
    // Create an async script element based on your key.
    var script = document.createElement("script");
    script.type = "text/javascript";
    script.async = true;
    // TODO we might want to add a check on the url to see if it ends with / or not
    script.src = unomiOption.url + "/tracker/unomi-tracker.js";

    if (script.addEventListener) {
      script.addEventListener("load", function (e) {
          if (typeof callback === "function") {
            callback(e);
          }
        }, false);
    } else {
      script.onreadystatechange = function () {
        if (this.readyState === "complete" || this.readyState === "loaded") {
          callback(window.event);
        }
      };
    }

    // Insert our script next to the first script element.
    var first = document.getElementsByTagName("script")[0];
    first.parentNode.insertBefore(script, first);
  };

  document.addEventListener("DOMContentLoaded", unomiTracker.load);

  unomiTracker.page(unomiOption.initialPageProperties);
})();
