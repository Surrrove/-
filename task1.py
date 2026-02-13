from __future__ import annotations

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    """
    Абстрактный способ оплаты.
    """

    def __init__(self, account_id: str, balance: float, active: bool) -> None:
        """
        Args:
            account_id: Идентификатор аккаунта (не пустой).
            balance: Баланс (>= 0).
            active: Активен ли способ оплаты.
        """
        if not isinstance(account_id, str) or not account_id.strip():
            raise ValueError("account_id must be a non-empty string")
        if balance < 0:
            raise ValueError("balance must be >= 0")

        self.account_id: str = account_id.strip()
        self.balance: float = float(balance)
        self.active: bool = bool(active)

    @abstractmethod
    def authorize(self, amount: float) -> bool:
        """
        Авторизовать сумму (без списания).

        Args:
            amount: Сумма (> 0).
        Returns:
            True если авторизация возможна, иначе False.
        """
        ...

    @abstractmethod
    def capture(self, amount: float) -> float:
        """
        Списать средства.

        Args:
            amount: Сумма (> 0).
        Returns:
            Новый баланс.
        """
        ...

    @abstractmethod
    def refund(self, amount: float) -> float:
        """
        Вернуть средства.

        Args:
            amount: Сумма (> 0).
        Returns:
            Новый баланс.

        Examples:
            >>> class DemoCard(PaymentMethod):
            ...     def authorize(self, amount: float) -> bool:
            ...         if amount <= 0:
            ...             raise ValueError("amount must be > 0")
            ...         return self.active and self.balance >= amount
            ...     def capture(self, amount: float) -> float:
            ...         if not self.authorize(amount):
            ...             raise ValueError("authorization failed")
            ...         self.balance -= amount
            ...         return self.balance
            ...     def refund(self, amount: float) -> float:
            ...         if amount <= 0:
            ...             raise ValueError("amount must be > 0")
            ...         self.balance += amount
            ...         return self.balance
            ...
            >>> card = DemoCard("ACC-1", 100.0, True)
            >>> card.capture(30.0)
            70.0
        """
        ...


class SmartDevice(ABC):
    """
    Абстрактное умное устройство.
    """

    def __init__(self, device_id: str, battery_level: float, online: bool) -> None:
        """
        Args:
            device_id: Идентификатор (не пустой).
            battery_level: Уровень заряда (0..1).
            online: Подключено ли устройство.
        """
        if not isinstance(device_id, str) or not device_id.strip():
            raise ValueError("device_id must be a non-empty string")
        if not (0.0 <= battery_level <= 1.0):
            raise ValueError("battery_level must be between 0 and 1")

        self.device_id: str = device_id.strip()
        self.battery_level: float = float(battery_level)
        self.online: bool = bool(online)

    @abstractmethod
    def connect(self) -> None:
        """
        Подключить устройство к сети.
        """
        ...

    @abstractmethod
    def perform_action(self, energy_cost: float) -> float:
        """
        Выполнить действие с затратой энергии.

        Args:
            energy_cost: Расход заряда (0..1).
        Returns:
            Новый уровень заряда.
        """
        ...

    @abstractmethod
    def charge(self, amount: float) -> float:
        """
        Зарядить устройство.

        Args:
            amount: Количество заряда (> 0).
        Returns:
            Новый уровень заряда (0..1).

        Examples:
            >>> class DemoLamp(SmartDevice):
            ...     def connect(self) -> None:
            ...         self.online = True
            ...     def perform_action(self, energy_cost: float) -> float:
            ...         if energy_cost <= 0:
            ...             raise ValueError("energy_cost must be > 0")
            ...         if energy_cost > self.battery_level:
            ...             raise ValueError("not enough battery")
            ...         self.battery_level -= energy_cost
            ...         return self.battery_level
            ...     def charge(self, amount: float) -> float:
            ...         if amount <= 0:
            ...             raise ValueError("amount must be > 0")
            ...         self.battery_level = min(1.0, self.battery_level + amount)
            ...         return self.battery_level
            ...
            >>> lamp = DemoLamp("LAMP-01", 0.5, False)
            >>> lamp.charge(0.3)
            0.8
        """
        ...


class LibraryItem(ABC):
    """
    Абстрактный элемент библиотеки (книга, журнал и т.д.).
    """

    def __init__(self, title: str, total_copies: int, available_copies: int) -> None:
        """
        Args:
            title: Название (не пустое).
            total_copies: Всего экземпляров (> 0).
            available_copies: Доступно (0..total_copies).
        """
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title must be a non-empty string")
        if total_copies <= 0:
            raise ValueError("total_copies must be > 0")
        if not (0 <= available_copies <= total_copies):
            raise ValueError("available_copies must be between 0 and total_copies")

        self.title: str = title.strip()
        self.total_copies: int = int(total_copies)
        self.available_copies: int = int(available_copies)

    @abstractmethod
    def borrow(self) -> bool:
        """
        Выдать экземпляр.

        Returns:
            True если успешно, иначе False.
        """
        ...

    @abstractmethod
    def return_item(self) -> bool:
        """
        Вернуть экземпляр.

        Returns:
            True если успешно, иначе False.
        """
        ...

    @abstractmethod
    def is_available(self) -> bool:
        """
        Проверить доступность.

        Returns:
            True если есть доступные экземпляры.

        Examples:
            >>> class DemoBook(LibraryItem):
            ...     def borrow(self) -> bool:
            ...         if self.available_copies <= 0:
            ...             return False
            ...         self.available_copies -= 1
            ...         return True
            ...     def return_item(self) -> bool:
            ...         if self.available_copies >= self.total_copies:
            ...             return False
            ...         self.available_copies += 1
            ...         return True
            ...     def is_available(self) -> bool:
            ...         return self.available_copies > 0
            ...
            >>> book = DemoBook("Clean Code", 3, 1)
            >>> book.borrow()
            True
            >>> book.is_available()
            False
        """
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)