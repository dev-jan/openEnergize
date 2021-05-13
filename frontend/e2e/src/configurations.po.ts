import { browser, by, element } from 'protractor';

export class ConfigurationsPage {
  async navigateTo(): Promise<unknown> {
    return browser.get(browser.baseUrl + '/configurations');
  }

  async getApiUrl(): Promise<string> {
    return element(by.css('app-configurationlist a')).getText();
  }

  async getBackendConfiguration(): Promise<string> {
    return element(by.css('app-configurationlist pre')).getText();
  }
}
