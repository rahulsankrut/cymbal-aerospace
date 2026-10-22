// Ensure src/data/mockData.ts is created before generating components that
// import from '../data/mockData'.
import React from 'react';

import {cardData} from '../data/mockData';

/**
 * Props for the ActivityCard component.
 */
export interface ActivityCardProps {
  readonly id?: string;
  readonly username?: string;
  readonly action?: 'MERGED' | 'COMMIT';
  readonly timestamp?: string;
  readonly avatarUrl?: string;
  readonly repoName?: string;
}

/**
 * Gold standard reference component rendering a repository activity card.
 */
export const ActivityCard: React.FC<Readonly<ActivityCardProps>> = ({
  username = cardData.username,
  action = cardData.action,
  timestamp = cardData.timestamp,
  avatarUrl = cardData.avatarUrl,
  repoName = cardData.repoName,
}) => {
  const isMerged = action === 'MERGED';

  return (
    <div className="flex items-center justify-between gap-4 rounded-lg bg-background-light dark:bg-background-elevated p-4 min-h-14 shadow-sm ring-1 ring-slate-900/10 dark:ring-white/10">
      <div className="flex items-center gap-4 overflow-hidden">
        <div
          className="aspect-square h-10 w-10 flex-shrink-0 rounded-full bg-cover bg-center bg-no-repeat"
          style={{backgroundImage: `url(${avatarUrl})`}}
          aria-label={`Avatar for ${username}`}
        />

        <div className="flex flex-wrap items-center gap-x-2 gap-y-1 text-sm sm:text-base">
          <a
            href="#"
            className="font-semibold text-primary dark:text-primary hover:underline truncate">
            {username}
          </a>

          <span
            className={`inline-block px-2 py-0.5 text-xs font-semibold rounded-full ${
              isMerged
                ? 'bg-accent-purple/20 text-accent-purple dark:bg-accent-purple/30 dark:text-accent-lavender'
                : 'bg-primary/20 text-primary dark:bg-primary/30 dark:text-primary'
            }`}>
            {action}
          </span>

          <span className="text-slate-600 dark:text-white/60">in</span>

          <a
            href="#"
            className="text-primary dark:text-primary hover:underline truncate">
            {repoName}
          </a>
        </div>
      </div>

      <div className="shrink-0">
        <p className="text-sm font-normal leading-normal text-slate-500 dark:text-white/50">
          {timestamp}
        </p>
      </div>
    </div>
  );
};
