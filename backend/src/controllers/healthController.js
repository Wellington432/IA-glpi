const healthService = require('../services/healthService');

class HealthController {
  index(req, res) {
    const response = healthService.status();

    return res.json(response);
  }
}

module.exports = new HealthController();