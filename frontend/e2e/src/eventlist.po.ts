import { browser, by, element } from 'protractor';

export class EventlistPage {
  async navigateTo(): Promise<unknown> {
    return browser.get(browser.baseUrl + '/eventlist');
  }

  async getReloadButtonText(): Promise<string> {
    return element(by.css('app-eventlist button')).getText();
  }
}
