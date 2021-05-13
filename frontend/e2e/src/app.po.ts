import { browser, by, element, ElementFinder } from 'protractor';

export class AppPage {
  async navigateTo(): Promise<unknown> {
    return browser.get(browser.baseUrl);
  }

  async getTitleText(): Promise<string> {
    return element(by.css('app-root .app-title')).getText();
  }

  async getNavigationEntries(): Promise<string> {
    return element.all(by.css('mat-nav-list span')).getText();
  }
}
