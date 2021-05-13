import { browser, by, element } from 'protractor';

export class OverviewPage {
  async navigateTo(): Promise<unknown> {
    return browser.get(browser.baseUrl + '/overview');
  }

  async getEnergySum(): Promise<string> {
    return element(by.css('app-overview .totals--card mat-card-title')).getText();
  }

  async getFirstProducerValue(): Promise<string> {
    return element.all(by.css('.device--container .producer--card mat-card-title')).first().getText();
  }

  async getProducers(): Promise<string> {
    return element.all(by.css('.device--container .producer--card')).getText();
  }

  async getStorages(): Promise<string> {
    return element.all(by.css('.device--container .storage--card')).getText();
  }

  async getConsumers(): Promise<string> {
    return element.all(by.css('.device--container .consumer--card')).getText();
  }
}
