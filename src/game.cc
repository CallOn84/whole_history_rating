#include "whr.h"
#include <cmath>
#include <cstdio>
#include <iostream>

namespace whr {

Game::Game(const std::shared_ptr<Player> white,
           const std::shared_ptr<Player> black, std::string winner,
           int time_step)
    : white_player_(white), black_player_(black), time_step_(time_step) {
  if (winner == "W") {
    winner_ = Winner::WHITE;
  } else if (winner == "B") {
    winner_ = Winner::BLACK;
  } else {
    winner_ = Winner::DRAW;
  }
}

double
Game::opponents_adjusted_gamma(const std::shared_ptr<Player> player) const {
  double opponent_elo;
  double rval = 0.;

  if (player == white_player_) {
    opponent_elo = bpd_->elo() - white_advantage;
  } else {
    opponent_elo = wpd_->elo() + white_advantage;
  }

  rval = std::pow(10., opponent_elo / 400.);
  return rval;
}

std::shared_ptr<Player> Game::opponent(const std::shared_ptr<Player> player) {
  if (player == white_player_) {
    return black_player_;
  } else {
    return white_player_;
  }
}

std::string Game::inspect() {
  char buffer[1000];
  std::snprintf(
      buffer, 1000, "Game: W:%s(%.2f) B:%s(%.2f) winner = %s",
      white_player_->get_name().c_str(), wpd_ ? wpd_->get_r() : 0.,
      black_player_->get_name().c_str(), bpd_ ? bpd_->get_r() : 0.,
      winner_ == Winner::WHITE ? "W" : (winner_ == Winner::BLACK ? "B" : "D"));
  return std::string(buffer);
}

double Game::likelihood() {
  switch (winner_) {
  case Winner::WHITE:
    return white_win_probability();
  case Winner::BLACK:
    return black_win_probability();
  default:
    return std::sqrt(white_win_probability() * black_win_probability());
  }
}

double Game::white_win_probability() {
  double gamma = wpd_->gamma();
  return gamma / (gamma + opponents_adjusted_gamma(white_player_));
}

double Game::black_win_probability() {
  double gamma = bpd_->gamma();
  return gamma / (gamma + opponents_adjusted_gamma(black_player_));
}

} // namespace whr
