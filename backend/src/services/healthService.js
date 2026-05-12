class HealthService {
  status() {
    return {
      status: 'online',
      api: 'IA-GLPI',
      version: '1.0.0'
    };
  }
}

module.exports = new HealthService();